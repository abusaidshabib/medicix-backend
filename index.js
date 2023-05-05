var express = require('express');
var cors = require('cors');
const { MongoClient, ServerApiVersion } = require('mongodb');
var app = express();
const port = process.env.PORT || 5000;
require('dotenv').config();

app.use(cors());
app.use(express.json());

const uri = process.env.DB_URI;
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverApi: ServerApiVersion.v1
});

async function dbConnect() {
  try {
    await client.connect();
    console.log("Database Connected")
  }

  catch (error) {
    console.log(error.name, error.message);
    res.send({
      success: false,
      error: error.message,
    })
  }
}

dbConnect();


const MEDICINE = client.db("medicix").collection("medicine");

app.get("/medicine", async (req, res) => {
  try {
    if (req.query.search) {
      const { search } = req.query;

      const medicine = await MEDICINE.find({
        $or: [
          { brand: { $regex: '.*' + search + '.*', $options: 'i' } },
          { generic: { $regex: '.*' + search + '.*', $options: 'i' } },
          { manufacturer: { $regex: '.*' + search + '.*', $options: 'i' } },
        ]
      }).limit(10).toArray();

      res.send({
        success: true,
        data: medicine,
      })
    }
    else if (req.query.expired) {
      const currentDate = new Date();
      const data = await MEDICINE.find({}).limit(1000).toArray();
      const nlength = await MEDICINE.find({}).toArray();

      const result = data?.filter(product => {
        const lastDate = new Date(product.lastdate);
        return lastDate < currentDate;
      });

      const length = nlength?.filter(product => {
        const lastDate = new Date(product.lastdate);
        return lastDate < currentDate;
      });

      res.send({
        success: true,
        data: result,
        length: length.length
      });
    }

    else if (req.query.stock) {
      const result = await MEDICINE.find({ totalProducts: { $lt: 50 } }).toArray();
      res.send({
        success: true,
        data: result,
        length: result?.length
      });
    }
    else if (req.query.field) {
      const result = await MEDICINE.updateMany({ quantity: { $exists: true } },
        { $set: { quantity: 1 } }
      )

      res.send({
        success: true,
        data: result,
      })
    }
    else {
      let query = {};
      const page = parseInt(req.query.page);
      const limit = parseInt(req.query.limit);
      const startIndex = (page - 1) * limit;

      const cursor = MEDICINE.find(query).skip(0).limit(400);
      const medicine = await cursor.toArray();
      const length = await MEDICINE.countDocuments({}, function (err, count) {
        return count;
      })

      res.send({
        success: true,
        data: medicine,
        length: length

      })
    }
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    });
  }
})


const SALES = client.db("medicix").collection("salesdata");

app.get("/sales/:year/:month", async (req, res) => {
  try {
    const year = req.params.year;
    const month = req.params.month;
    const cursor = SALES.find({ date: { $regex: `^[0-9]{2}-${month}-${year}$` } });
    const result = await cursor.toArray();

    res.send({
      success: true,
      data: result,
      length: result.length
    })
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    })
  }
})


const HIGH = client.db("medicix").collection("highsales");

app.get("/high/:year/:month", async (req, res) => {
  try {
    const year = req.params.year;
    const month = req.params.month;
    const result = await HIGH.findOne({ month: { $regex: `${month}-${year}$` } });

    res.send({
      success: true,
      data: result?.data?.sort((a, b) => b.totalsales - a.totalsales),
    })
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    })
  }
})

const INVOICE = client.db('medicix').collection("invoice");
app.get("/invoice", async (req, res) => {
  try {
    const result = await INVOICE.find({}).toArray();

    res.send({
      success: true,
      data: result.reverse().slice(0, 5),
      length: result.length
    })
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    })
  }
})


app.get("/members", async (req, res) => {
  try {

    const cursor = INVOICE.find({});
    const invoice = await cursor.toArray();

    const result = invoice.reduce((acc, current) => {
      const x = acc.find(item => item.name === current.name);
      if (!x) {
        return acc.concat([current]);
      } else {
        return acc;
      }
    }, []);

    res.send({
      success: true,
      data: result,
      length: result?.length
    });
  }

  catch (error) {
    res.send({
      success: false,
      data: error.message
    })
  }
})

app.post("/invoice/post", async (req, res) => {
  try {
    const invoice = req.body;

    const result = await INVOICE.insertOne(invoice);

    res.send({
      success: true,
      data: result
    });
  }
  catch (error) {

    res.send({
      success: false,
      data: error.message
    })

  }
})




app.get('/', async (req, res) => {
  res.send("Medicix Backend running")
})

app.listen(port, () => {
  console.log(`Medicix Backend running on port ${port}`)
})