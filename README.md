# PDA Availability Checker
Checks the WA Department of Transport Practical Driving Assessment Bookings availability. 

This was made very quick so there may be some issues, it definitely could be refined. But was just for a mate so instead of refreshing the DOT page every few minutes and having to go through each step and menu to check availability, this just printed out the list.  

I suggest having this run on a schedule, or what I did was embed it in a Discord bot to output the availability list in an embed. Whatever floats your boat. 

Requirements
- Selenium 
- Python 3.x

I used the Firefox driver but of course you can change it to whatever you like. 

Run like so: 

`python pda.py --permitnum YOURPERMITNUMBER --expiry DD/MM/YYYY --firstname YOURFIRSTNAME --lastname YOURLASTNAME --dob DD/MM/YYYY`

Expected output: 

```
...
DOT Success has availability: 08/06/2020 at 7:05 AM
DOT Success has availability: 08/06/2020 at 2:50 PM
DOT Success has availability: 10/06/2020 at 7:05 AM
DOT Success has availability: 10/06/2020 at 7:55 AM
DOT Welshpool has no availability
DOT West Perth has availability: 08/06/2020 at 10:35 AM
DOT West Perth has availability: 08/06/2020 at 11:25 AM
DOT West Perth has availability: 08/06/2020 at 1:00 PM
DOT West Perth has availability: 08/06/2020 at 1:50 PM
DOT West Perth has availability: 09/06/2020 at 7:55 AM
...
```
Limitations: 
 - Class C Only (Well whatever is selected by default)
 - Driving Instructor Bookings 
 - Overseas Licence Bookings 
 - Single Name Bookings 
 - Earliest Availability Only 
 - Metro Only 
 
(Maybe later idk)
 
 Sleeps all over the place or page won't load quick enough. If your internet is fast enough yeah sure but even then might not be able to keep up. 
 
 Not liable for any damages, don't spam the DOT.
