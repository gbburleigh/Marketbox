function generateUserID(){
    let min = 10000000;
    let max = 99999999;
    return Math.floor(Math.random() * (max - min) + min);
}

export default generateUserID;