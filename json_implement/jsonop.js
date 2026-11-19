console.log("This is my json operations");
    const json =`{
                    "name" : "Dilkash",
                    "phone" : "9812345678",

                    "skills" : ["java","Python"],

                    "address" : 
                    {
                        "city" : "janakpur",
                        "pincode" : 2354
                    }
         }`;

// show json values
// console.log(json)  

// parse this json to perform operations

const user = JSON.parse(json)
// console.log(typeof json)    
// console.log(typeof user)


// show values of json
console.log(user.name)
console.log(user.phone)
console.log(user.skills)

console.log(user.address.city)
console.log(user.address.pincode)


// javascript code
const todo = {
    title: "learn django",
    isSkilled : true
};

//convert js object to json string.
const jsonTodo = JSON.stringify(todo)
console.log(jsonTodo)