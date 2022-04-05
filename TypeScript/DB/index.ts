const { MongoClient, ServerApiVersion } = require('mongodb');

const uri = "mongodb+srv://kishore:kishore&2104@cluster0.sciwm.mongodb.net/test_db?retryWrites=true&w=majority";

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });

client.connect((err: any) => {
  const collection = client.db("test").collection("devices");
  console.log('Server has connected')
  // perform actions on the collection object
  client.close();
});
