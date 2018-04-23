# beacon

Beacon is a  small software to make a beacon utilizing Bluetooth. The ID is unique using a uuid4.

The is send after generation and can be detected to a device.

It is possible to gernarate a distance detection to trianbulate a mobile device using different beacons.

I did use the first version of this software to triangulate my position in a production shopfloor.

```python
import beacon

check_user()
check_device("hci0")

bc = Beacon("hci0")
bc.config()
bc.start("01","7c") // dai
```
