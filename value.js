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



function generateRandomNumbers() {
  let randomNumber1 = 0;
  let randomNumber2 = 0;
  let randomNumber3 = 0;

  // Generate randomNumber1 and randomNumber2 until randomNumber1 is larger than randomNumber2
  do {
    randomNumber1 = Math.floor(Math.random() * 100) + 50; // generates a random number between 50 and 149
    randomNumber2 = Math.floor(Math.random() * 100); // generates a random number between 0 and 99
  } while (randomNumber1 <= randomNumber2);

  // Generate randomNumber3 between 600 and 1200
  randomNumber3 = Math.floor(Math.random() * 601) + 600; // generates a random number between 600 and 1200

  let resultString1 = randomNumber1; // convert the first random number to a string
  let resultString2 = randomNumber2; // convert the second random number to a string
  let resultString3 = randomNumber3; // convert the third random number to a string

  return { resultString1, resultString2, resultString3 };
}


const MEDICINE = client.db("medicix").collection("medicine");

app.get("/medicine", async (req, res) => {
  try {
    const page = parseInt(req.query.page);
    const limit = parseInt(req.query.limit);
    const startIndex = (page - 1) * limit;

    const cursor = MEDICINE.find({}).skip(0).limit(365);
    const medicine = await cursor.toArray();

    res.send({
      success: true,
      data: medicine,
    });
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    });
  }
})

app.post("/medicine/post", async (req, res) => {

  try {

    const base = await MongoClient.connect(uri, { useUnifiedTopology: true });
    const db = base.db('medicix');
    const collection = db.collection('salesdata');

    const newData = [];
    const cursor = collection.find({});
    await cursor.forEach(doc => {
      newData.push({ _id: doc._id, date: printDatesOfYear(2021) });
    });

    // const result = generateRandomNumbers();

    const result = await Promise.all(newData.map(doc => {
      return collection.updateOne({
        _id: doc._id
      },
        {
          $set: {
            date: doc.date
          }
        }
      )
    }))

    res.send({
      success: true,
      data: result
    })

  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    });
  }
})

app.post("/medicine", async (req, res) => {
  try {

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
    })
  }
  catch (error) {
    res.send({
      success: false,
      data: error.message,
    })
  }
})



app.get('/', async (req, res) => {
  res.send("Medicix Backend running")
})

app.listen(port, () => {
  console.log(`Medicix Backend running on port ${port}`)
})
