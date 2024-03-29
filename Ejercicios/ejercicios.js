var x = 10
console.log(x)
var name
console.log(name)
function ejemploVar(){
    for(var j = 0;j<3;j++){
        console.log(j)
    }
    console.log(j)
}
console.log(ejemploVar())
function ejemplolet(){
    let w = 10;
    if(true){
        let w = 20;
        console.log(w)
    }
    console.log(w)
}
console.log(ejemplolet())
const Tax_Rate = 0.1;
const person ={
    name: 'jhon',
    age: 30
};
console.log(person)
person.age =31;
console.log(person)
