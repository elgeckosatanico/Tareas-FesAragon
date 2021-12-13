/* A-1
Indicar cual es el que falta */
const total=45;
const arr=[0,1,2,4,5,6,7,8,9];
let aux = 0 //sum arr

let i=0;
for(i=0; i<arr.length; i++){
    aux += arr[i]
}

if(total==aux && arr.length>=10){
    console.log("No falta ninguno")
}else{
    console.log('Falta el número', (total - aux))
}