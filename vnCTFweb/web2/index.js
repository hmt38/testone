const express = require("express");
const path = require("path");
const vm2 = require("vm2");

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static("static"));

const vm = new vm2.NodeVM();

app.use("/eval", (req, res) => {
  const e = req.body.e;
  if (!e) {
    res.send("wrong?");
    return;
  }
  try {
    res.send(vm.run("module.exports="+e)?.toString() ?? "no");
  } catch (e) {
    console.log(e)
    res.send("wrong?");
  }
});

app.use("/flag", (req, res) => {
  if(Object.keys(Object.prototype).length > 0) {
    Object.keys(Object.prototype).forEach(k => delete Object.prototype[k]);
    res.send(process.env.FLAG);
  } else {
    res.send(Object.keys(Object.prototype));
  }
})

app.use("/source", (req, res) => {
  let p = req.query.path || "/src/index.js";
  p = path.join(path.resolve("."), path.resolve(p));
  console.log(p);
  res.sendFile(p);
});

app.use((err, req, res, next) => {
  console.log(err)
  res.redirect("index.html");
});

app.listen(process.env.PORT || 8888);