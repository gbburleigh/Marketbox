const mongoose = require('mongoose');

const auctionSchema = mongoose.Schema({
    auctionSeller: {
        type: String,
        required: true
    },
    auctionName: {
        type: String,
        required: true
    },
    auctionPostDate:{
        type: Date,
        required: true,
        default: Date.now
    },
    auctionActiveStatus:{
        type: Boolean,
        required: true,
        default: true
    }
})

module.exports = mongoose.model('Auction', auctionSchema)