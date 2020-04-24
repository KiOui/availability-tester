# availability-tester
An availability tester made for displaying the status of HTTP(s) servers on a Raspberry Pi connected to an [Allo Mini Rainbow](https://thepihut.com/products/allo-mini-rainbow-phat-8x4-led-matrix). The allo mini rainbow will display whether a site is online/offline and will show text when a status of a website changes. It just does normal http(s) requests and sees if a ```200 OK``` is returned.

## Installation
1. First install the required ```Rainbow HAT``` package from [here](https://github.com/allocom/Rainbow-HAT).
2. In ```availability-tester/run.py``` you can change the ```SITES``` variable and the ```BRIGHTNESS``` variable to suit your needs.
3. Execute ```run.py``` to run the tester. Stop it with ```Control-C```.