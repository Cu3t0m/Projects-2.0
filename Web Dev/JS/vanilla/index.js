#!/usr/bin/env node

// sqlite.js
const sqlite3 = require('sqlite3').verbose()
let db = new sqlite3.Database(':memory:', (err) => {
    if (err) {
        return console.log("Error:", err.message)
    }
    console.log("Connected to DB")
})
db.close()