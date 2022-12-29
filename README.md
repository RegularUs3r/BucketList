# BucketList - Any last whishes ?

## :spider: BucketList was created, mainly due my curiosity, but also to help anyone to download files from open aws' buckets, with an excuse to analyze them locally.


### :gear: Instalation
      pip install -r requirements.txt

### :man_technologist: Usage 
      ./BucketList.py 
      Created By: SickAndTired

      You should pick a mode
       │ 
       └──────[cct-fuzz]
       │ 
       └──────[xml]

### :heavy_exclamation_mark: fuzz mode is yet to come !
_________________________________________       
       
      $./BucketList.py xml -h
      Created By: SickAndTired

      usage: BucketList.py [-h] -t [-v] [ ...]

      Created By: SickAndTired

      positional arguments:


      optional arguments:
        -h, --help        show this help message and exit
        -t, --target  target.com
        -v, --verbose
        
_________________________________________

### :receipt: Example
       ./BucketList.py xml -v -t http://some-target-bucket.s3-sa-east-1.amazonaws.com/


#### :warning: Disclaimer! - Only use it under prior authorization of the target. I do not take any responsibility for its use. :warning:
      
