//Remove dotenv package dependency for deployment
if (process.env.NODE_ENV !== 'production'){
    require('dotenv').config()
}

if (process.env.GENERATE_FRESH_TOKEN === 'true') {
    process.env.ACCESS_TOKEN_SECRET=require('crypto').randomBytes(64).toString('hex')
}

//Express/app object declaration
const express = require('express');
const app = express();
const jwt = require('jsonwebtoken')

//Dependency declarations
const expressLayouts = require('express-ejs-layouts')
const bodyParser = require('body-parser')

const userRouter = require('./routes/users')
const auctionRouter = require('./routes/auctions')
const indexRouter = require('./routes/index')

//App config + dependency init
app.set('view engine', 'ejs')
app.set('views', __dirname + '/views')
app.set('layout', 'layouts/layout')
app.use(expressLayouts)
app.use(express.json())
app.use(express.static('public'))
app.use(bodyParser.urlencoded({ limit: '10mb', extended: false}))
app.use(express.static(__dirname + '/public'));

//DB Connect
const mongoose = require('mongoose')
mongoose.connect(process.env.DATABASE_URL, { 
    useNewUrlParser: true,
    useUnifiedTopology: true
})

//Log status upon active connection
const db = mongoose.connection
db.on('error', error => console.error(error))
db.once('open', () => console.log('Connected to Mongoose'))

app.use('/', indexRouter)
app.use('/users', userRouter)
app.use('/auctions', auctionRouter)

app.listen(process.env.POST || 3000)