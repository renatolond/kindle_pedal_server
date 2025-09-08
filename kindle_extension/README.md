Kindle Extension
=====

This is a KUAL extension that opens the iptables port 8000 and then starts a Python server on that port.

Once the server is started it can only be stopped by restarting the Kindle or going into the Kindle using SSH and killing the server from there. This might be improved at some point.

To install, copy the folder into the extensions folder in the kindle.

This requires Python 3.x to be installed in the kindle. Something like [Python 3.11 for HF devices](https://www.mobileread.com/forums/showpost.php?p=4506311&postcount=1) can be used, depending on your Kindle model.

The `b.txt` and the `f.txt` were generated in the kindle. With a book open in the kindle, I ran:

```sh
cat /dev/input/event1 > f.txt
```

Then, I pushed the screen once to make the page go forward. I then hit ctrl+C and did the same for backwards.
