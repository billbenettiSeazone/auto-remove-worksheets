# Auto remove worksheets
Python script to remove worksheets on the Airbnb_01 SpreadSheet.

The script removes the sheets **"Datas Livres"** and **"TO"**, that contais long terms of VBA Scripts.

## Running
> Download the .xlsx file into a selected path
> - Clone this project
> - Navigate to the path you cloned
> - Run the following commands:
```
pip3 install -r requirements.txt
```
> - Make run.sh an executable file with: 
``` bash
chmod +x job.sh
```
> - Then run:
```bash
./remove
``` 
> - **OR** execute directly with:
``` bash
python3 tab_remove.py /path/to/your/file
```
