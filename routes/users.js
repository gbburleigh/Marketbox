const express = require('express')
const router = express.Router()
const User = require('../models/User')

//GET method for all users
router.get('/users/all', async (req, res) => {
    try{
        res.render('users/all')
        const users = await User.find()
        res.json(users)
    }
    catch(err){
        res.status(500).json({ message: err.message})
    }
})

//GET method for specific user object
router.get('/users/:id', async (req, res) => {
    try{
        res.render('users/:id')
        const users = await User.find()
        res.json(users)
    }
    catch(err){
        res.status(500).json({ message: err.message})
    }
})

//POST method for creating user object
router.post('/users/all', (req, res) => {
    const user = new User({
        username: req.body.username,
        password: req.body.password,
        email: req.body.email
    })
    user.save((err, newUser) => {
        if(err){
            res.render('users/new', {
                user: user,
                errorMsg: 'Error creating User'
            })
        }
        else {
            //res.redirect('users/${newUser.id}')
        }
    })
})

//Update user route
router.patch('/:id', (req, res) => {
    
})

//Delete user route
router.delete('/:id', (req, res) => {

})

module.exports = router