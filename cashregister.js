var cashRegister = {
total:0,
add: function(itemCost){
    this.total += itemCost;
},
scan: function(item) {
        switch (item, quantity) {
        case "eggs": this.add(0.98 * quantity); break;
        case "milk": this.add(1.23 * quantity); break;
        case "magazine": this.add(4.99 * quantity); break;
        case "chocolate": this.add(0.45 * quantity); break;
    }
}
};

// scan each item 4 times
cashRegister.add("eggs", 4);
cashRegister.add("milk", 4);
cashRegister.add("magazine", 4);
cashRegister.add("chocolate", 4);


//Show the total bill
console.log('Your bill is '+ cashRegister.total);