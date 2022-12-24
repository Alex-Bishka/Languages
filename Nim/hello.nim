import std/[
    httpclient, net, json, jsonutils, strutils
]
import strformat    # formatting strings

# check this out :)

# define your one types
type
    Name = string
    Age = Natural
    Day = Natural
    Month = string
    Year = Natural
    Bday = tuple
        month: Month
        day: Day
        year: Year

# vars don't need annotations, but it's cool
var
    name: Name = "Jeff"
    age: Age = 30
    month: Month = "October"
    day: Day = 21
    year: Natural = 1992
    bday: Bday = (month: month, day: day, year: year)

# bind vars once - immutable
let
    home: string = "Boston"

# computed at compile time
const
    cond: bool = true

#[
    Two ways to run:
        1. Compile the file with `nim c <file_name>` and run it via `./<file_name>`
        2. To complie and run immediately, add the -r flag: `nim c -r <file_name>`
]# 

echo "\nHello\n"

const msg = "My name is {name}, and I am {age} years old"
echo fmt(msg)

let alex_bday = bday
const bday_msg = "My birthday is {alex_bday.month} {alex_bday.day}th, {alex_bday.year}\n"
echo fmt(bday_msg)

# example function
type Output = int
proc exponent(base: int, power: int): Output =
    if power == 0:
        return 1
    else:
        return base * exponent(base, (power - 1))

echo fmt("2 sqaured is {exponent(2, 2)}")
echo fmt("2 cubed is {exponent(2, 3)}\n")

# api calls
let client = newHttpClient()
let response = client.request("http://google.com", httpMethod = HttpGet)
echo fmt("Get request status: {response.status}\n")
echo client.getContent("http://google.com")