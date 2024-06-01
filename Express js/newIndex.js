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
      }).toArray();

      res.send({
        success: true,
        data: medicine,
      })
    }
    // else if (req.query.expired) {
    //   const currentDate = new Date();
    //   const day = currentDate.getDate();
    //   const month = currentDate.getMonth() + 1;
    //   const year = currentDate.getFullYear();
    //   // const today = ;
    //   const result = await MEDICINE.find({
    //     lastdate: { $lte: "17-8-2023" }
    //   }).limit(1000).toArray();

    //   res.send({
    //     success: true,
    //     data: result,
    //     length: result?.length
    //   });
    // }

    else if (req.query.stock) {
      const result = await MEDICINE.find({ quantity: { $lt: 50 } }).toArray();
      res.send({
        success: true,
        data: result,
        length: result?.length
      });
    }
    else {
      let query = {};
      const page = parseInt(req.query.page);
      const limit = parseInt(req.query.limit);
      const startIndex = (page - 1) * limit;

      const cursor = MEDICINE.find(query).skip(0).limit(365);
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


app.get("/medicine/expired", async (req, res) => {
  try {
    const currentDate = new Date();
    const day = currentDate.getDate();
    const month = currentDate.getMonth() + 1;
    const year = currentDate.getFullYear();
    const today = `${day}-${month}-${year}`;
    const result = await MEDICINE.find({
      lastdate: { $lt: today }
    }).limit(1000).toArray();

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
      data: result.reverse(),
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



app.get('/', async (req, res) => {
  res.send("Medicix Backend running")
})

app.listen(port, () => {
  console.log(`Medicix Backend running on port ${port}`)
})