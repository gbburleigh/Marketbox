const express = require('express')
const router = express.Router()
const Auction = require('../models/Auction')

//GET method for all aucitons
router.get('/auctions', async (req, res) => {
    try{
        res.render('auctions/all')
        const auctions = await Auction.find()
        res.json(auctions)
    }
    catch(err){
        res.status(500).json({ message: err.message})
    }
})

//GET method for specific user object
router.get('/auctions/:id', async (req, res) => {
    try{
        res.render('auctions/:id')
        const auctions = await Auctions.find()
        res.json(auctions)
    }
    catch(err){
        res.status(500).json({ message: err.message})
    }
})

//POST method for creating user object
router.post('/auctions', (req, res) => {
    const auction = new Auction({
        auctionSeller: req.body.seller,
        auctionName: req.body.name,
    })
    auction.save((err, newAuction) => {
        if(err){
            res.render('auctions/new', {
                user: user,
                errorMsg: 'Error creating Auction'
            })
        }
        else {
            //res.redirect('auctions/${newAuction.id}')
        }
    })
})

//Update auction route
router.patch('/:id', (req, res) => {
    
})

//Delete auction route
router.delete('/:id', (req, res) => {

})

module.exports = router