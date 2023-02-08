# Evan Richardson and Malik Walker's AirBnB_clone

## Welcome the the holbertonschool-AirBnB_clone Project!
In this readme I shall try and give a brief explanation/overview of our project for you.


## How to access the console:
*Make sure files have executable permissions*
```
$./console.py
(hbnb) 
```
If you see "(hbnb) " that means you have successfully entered the console.

## Some examples of commands:
The do_create/create command and do_all/all command:
```
$./console.py
(hbnb) create BaseModel
c723ec3c-4ce6-4d7b-bbbe-6a016c506e71
(hbnb) all BaseModel
["[BaseModel] (8f3defa5-a90b-4cac-b786-cfb5f9028137) {'id': '8f3defa5-a90b-4cac-b786-cfb5f9028137', 'created_at': datetime.datetime(2023, 2, 6, 15, 13, 41, 816640), 'updated_at': datetime.datetime(2023, 2, 6, 15, 13, 41, 912910), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (bbf2b7f6-e906-44a2-8f5a-68ac5dae61c6) {'id': 'bbf2b7f6-e906-44a2-8f5a-68ac5dae61c6', 'created_at': datetime.datetime(2023, 2, 6, 18, 45, 47, 621395), 'updated_at': datetime.datetime(2023, 2, 6, 18, 45, 47, 621408), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (0ec138d2-4cb1-4897-b62e-364c99e609b0) {'id': '0ec138d2-4cb1-4897-b62e-364c99e609b0', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 929674), 'updated_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 929674)}", "[BaseModel] (6e0a7c53-777b-4d0e-babe-ea7ec94e1508) {'id': '6e0a7c53-777b-4d0e-babe-ea7ec94e1508', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 930306), 'updated_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 930306)}", "[BaseModel] (814ef4e5-0a6c-4902-b160-0114b16f748e) {'id': '814ef4e5-0a6c-4902-b160-0114b16f748e', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 930656), 'updated_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 930656)}", "[BaseModel] (27d736ea-db1e-4aa2-b6e8-3da08326fb25) {'id': '27d736ea-db1e-4aa2-b6e8-3da08326fb25', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 931127), 'updated_at': 
datetime.datetime(2023, 2, 6, 18, 47, 41, 931127)}", "[BaseModel] (4f9f312c-6319-4fde-846d-31272e6d9f37) {'id': '4f9f312c-6319-4fde-846d-31272e6d9f37', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 931743), 'updated_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 931743)}", 
"[BaseModel] (8897521d-92d9-4f5f-a26e-d8303e49981c) {'id': '8897521d-92d9-4f5f-a26e-d8303e49981c', 'created_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 932696), 'updated_at': datetime.datetime(2023, 2, 6, 18, 47, 41, 932704)}", "[BaseModel] (98261eb4-b544-48ae-b4b7-064fd1d646d4) {'id': '98261eb4-b544-48ae-b4b7-064fd1d646d4', 'created_at': datetime.datetime(2023, 2, 7, 12, 58, 22, 923504), 'updated_at': datetime.datetime(2023, 2, 7, 12, 58, 22, 923521)}", "[BaseModel] (c723ec3c-4ce6-4d7b-bbbe-6a016c506e71) {'id': 'c723ec3c-4ce6-4d7b-bbbe-6a016c506e71', 'created_at': datetime.datetime(2023, 2, 7, 13, 10, 27, 956815), 'updated_at': datetime.datetime(2023, 2, 7, 13, 10, 27, 956837)}"]
(hbnb) 
```
Let's show off the do_update/update command:
```
(hbnb) update BaseModel c723ec3c-4ce6-4d7b-bbbe-6a016c506e71 first_name "Betty"
(hbnb) show BaseModel c723ec3c-4ce6-4d7b-bbbe-6a016c506e71
[BaseModel] (c723ec3c-4ce6-4d7b-bbbe-6a016c506e71) {'id': 'c723ec3c-4ce6-4d7b-bbbe-6a016c506e71', 'created_at': datetime.datetime(2023, 2, 7, 13, 10, 27, 956815), 'updated_at': datetime.datetime(2023, 2, 7, 13, 10, 27, 956837), 'first_name': '"Betty"'}
(hbnb) 
```
and now the do_destroy/destroy command:
```
(hbnb) destroy
** class name missing **
```
OOPS! Forgot to add something for it to destroy~!
```
(hbnb) destroy BaseModel c723ec3c-4ce6-4d7b-bbbe-6a016c506e71
(hbnb) 
```
Now what happens if we try and use the do_show/show command?:
```
(hbnb) show BaseModel c723ec3c-4ce6-4d7b-bbbe-6a016c506e71
** no instance found **
(hbnb) 
```
Now enough examples.

## Files for the console:
| File  | Description |
| ------------- |:-------------:|
| models/engine/file_storage.py | Our storage management system for specifically files |
| models/amenity.py | This subclass is for Amenities |
| models/city.py | This subclass is for Cities |
| models/place.py | This subclass is for Places |
| models/review.py | This subclass is for Reviews |
| models/state.py | This subclass is for States |
| models/user.py | This subclass is for Users |
| models/base_model.py | This is the base class that brings everything together for the console |
| Honorable | Mentions |
| __init__.py | This is what packages everything togeter ;) |
| tests/* | All the test files are very important for catching bugs! |

## Links

https://github.com/evanrich2404/holbertonschool-AirBnB_clone
> This is where you should have found this or through Malik's page
https://github.com/Wolverine5696



# End of README.md
