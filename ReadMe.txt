The code can be raun using "python swimselect.py" to run the program. The flag -h can be used to access a small help menu

Example of select:
python3 swimselect.py -select type -where ipv4

This selection will select the field of type and only where it matches to ipv4

Design notes:
One thing I could change is having the ability to have multiple select options, however at that point I would rather use SQLite. 
I did not use SQLite as the limitation was try to make everything from scratch as much as possible.
Results is not automatically deleted because I feel like it is helpful. 
If i were to use sql, then it would definitely cache all results and searches.

Another design flaw is how the program gets RDAP and GeoIP. I had to rely on free databases, so access amounts and having to wait on time is an issue that would be solved by having the more reliable databases readily available.


Shortlist is a shorter list of 40 to be tested on the program. 