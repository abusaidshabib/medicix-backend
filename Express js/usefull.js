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

app.post("/medicine/post", async (req, res) => {

  try {

    const base = await MongoClient.connect(uri, { useUnifiedTopology: true });
    const db = base.db('medicix');
    const collection = db.collection('medicine');

    const newLastDates = [];
    const cursor = collection.find({});
    await cursor.forEach(doc => {
      newLastDates.push({ _id: doc._id, lastdate: generateRandomDate() });
    });

    // const result = newLastDates.length;

    const result = await Promise.all(newLastDates.map(doc => {
      return collection.updateOne({
        _id: doc._id
      },
        {
          $set: {
            lastdate: doc.lastdate
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


function printDatesOfYear(year) {
  // Loop through each day of the year
  for (let month = 0; month < 12; month++) {
    for (let day = 1; day <= 31; day++) {
      // Create a new Date object for the current day
      const date = new Date(year, month, day);

      // Check if the current day is a valid date
      if (date.getMonth() === month) {
        // Output the date in DD-MM-YYYY format
        const dateString = `${date.getDate().toString().padStart(2, '0')}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getFullYear()}`;
        console.log(dateString);
      }
    }
  }
}


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


app.get("/unique", async (req, res) => {
  try {

    const cursor = await MEDICINE.find({}).limit(365);
    const medicine = await cursor.toArray();

    const result = medicine.reduce((acc, current) => {
      const x = acc.find(item => item.generic === current.generic);
      if (!x) {
        return acc.concat([current]);
      } else {
        return acc;
      }
    }, []);

    res.send({
      success: true,
      data: result,
    });
  }

  catch (error) {
    res.send({
      success: false,
      data: error.message
    })
  }


})



app.post("/medicine/post", async (req, res) => {

  try {

    const base = await MongoClient.connect(uri, { useUnifiedTopology: true });
    const db = base.db('medicix');
    const collection = db.collection('medicine');

    const newData = [];
    const cursor = collection.find({});
    await cursor.forEach(doc => {
      newData.push({ _id: doc._id, price: generateRandomNumbers().resultString1, revenue: generateRandomNumbers().resultString2, quantity: generateRandomNumbers().resultString3 });
    });

    // const result = generateRandomNumbers();

    const result = await Promise.all(newData.map(doc => {
      return collection.updateOne({
        _id: doc._id
      },
        {
          $set: {
            price: doc.price,
            revenue: doc.revenue,
            quantity: doc.quantity
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


















if (req.query.search) {
  query = { search: req.query.search }

  const medicine = await MEDICINE.find({ $text: { $search: search } }).toArray();

  res.send({
    success: true,
    data: medicine,
    length: length

  })
}
else if (req.query.expired) {

  const currentDate = new Date();
  const day = currentDate.getDate();
  const month = currentDate.getMonth() + 1;
  const year = currentDate.getFullYear();
  const today = `${day}-${month}-${year}`;
  const result = await MEDICINE.find({
    lastdate: { $lte: (today) }
  }).limit(1000).toArray();

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



db.collection('medicines').insertMany(medicines, function (err, result) {
  if (err) throw err;

  console.log(`${result.insertedCount} documents inserted into medicines collection`);

  // create text index on brand and generic fields
  db.collection('medicines').createIndex({ brand: "text", generic: "text" }, function (err, result) {
    if (err) throw err;

    console.log("Text index created on brand and generic fields");

    // search for documents that contain the word "Nimocon" in either the brand or generic fields
    db.collection('medicines').find({ $text: { $search: "Nimocon" } }).toArray(function (err, result) {
      if (err) throw err;

      console.log(`${result.length} documents found containing the word "Nimocon":`);
      console.log(result);

      client.close();
    });
  });
});
});