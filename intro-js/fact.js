var phones=[
    {model: "walton", price:1500, rom:"6GB"},
    {model: "samsung", price:15050, rom:"8GB"},
    {model: "Vivo", price: 8000, rom:"5GB"},
];
cheap=phones[0];
for (var element of phones){
    if(element.price<cheap.price){
        cheap=element;
    }
}
console.log(cheap);


