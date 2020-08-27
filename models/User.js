const mongoose = require('mongoose');


const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        min: 6,
        max: 512
    },
    password: {
        type: String,
        required: true,
        min: 6,
        max: 1024
    },
    email: {
        type: String,
        required: true,
        min: 12,
        mmax: 1024
    },
    activeAuctions: {
        type: [],
        required: true,
        default: []
    },
    pastAuctions: {
        type: [],
        required: true,
        default: []
    },
    databaseID: {
        type: Number,
        required: true,
        default: (() => {
            let min = 10000000;
            let max = 99999999;
            return Math.floor(Math.random() * (max - min) + min);
        })
    }
})

module.exports = mongoose.model('User', userSchema);