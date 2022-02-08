var http = require('http');
var os=require('os');

var ifaces=os.networkInterfaces();

//create a server object:
http.createServer(function (req, res) {
    
    for (var dev in ifaces) {
        var alias=0;
        ifaces[dev].forEach(function(details){
        if (details.family=='IPv4') {
            res.write('Hello DevOps Practitioner from ' + dev + ' ip' + details.address + '\n');
            console.log(details);
            ++alias;
        }
        });
    }
    res.end(); //end the response   
}).listen(80); //the server object listens on port 80

