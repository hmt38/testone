webpackJsonp([1],{"0jU9":function(t,e){},NHnr:function(t,e,l){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=l("7+uW"),s={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var i=l("VU/8")({name:"App"},s,!1,function(t){l("gsu9")},null,null).exports,n=l("/ocq"),r=l("mtWM"),o=l.n(r).a.create({baseURL:"/",timeout:5e3});var c={data:function(){return{flag:1,form:{input:""},result:""}},methods:{ClickPing:function(){this.result="",this.flag=1},ClickTraceroute:function(){this.result="",this.flag=2},ClickFTPCheck:function(){this.result="",Submit3()},ClickShellCheck:function(){this.result="",this.flag=4},Submit1:function(){var t,e=this;(t=this.form.input,o({url:"/ping",method:"post",data:{addr:t}})).then(function(t){console.log(t.data),e.result=t.data})},Submit2:function(){var t,e=this;(t=this.form.input,o({url:"/traceroute",method:"post",data:{addr:t}})).then(function(t){console.log(t.data),e.result=t.data})},Submit3:function(){var t=this;o({url:"/ftpcheck",method:"get"}).then(function(e){console.log(e.data),t.result=e.data})},Submit4:function(){var t,e=this;(t=this.form.input,o({url:"/shellcheck",method:"post",data:{shell:t}})).then(function(t){console.log(t.data),e.result=t.data})}}},u={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("el-row",[a("img",{staticClass:"logo",staticStyle:{width:"150px",height:"150px"},attrs:{src:l("tGse"),alt:""}}),t._v(" "),a("div",{staticClass:"h1"},[t._v("NETWORK TOOLS")])]),t._v(" "),a("el-row",[a("el-col",{attrs:{span:6,offset:3}},[a("el-row",{staticClass:"row-bg",attrs:{type:"flex",gutter:"20"}},[a("div",[a("el-button",{attrs:{type:"primary",plain:""},on:{click:t.ClickPing}},[t._v("Ping")])],1)]),t._v(" "),a("el-row",{staticClass:"row-bg",attrs:{type:"flex",gutter:"20"}},[a("div",{staticClass:"grid-content"},[a("el-button",{attrs:{type:"success",plain:""},on:{click:t.ClickTraceroute}},[t._v("Traceroute")])],1)]),t._v(" "),a("el-row",{staticClass:"row-bg",attrs:{type:"flex",gutter:"20"}},[a("div",{staticClass:"grid-content"},[a("el-button",{attrs:{type:"info",plain:""},on:{click:t.ClickFTPCheck}},[t._v("FTP Check")])],1)]),t._v(" "),a("el-row",{staticClass:"row-bg",attrs:{type:"flex",gutter:"20"}},[a("div",{staticClass:"grid-content"},[a("el-button",{attrs:{type:"warning",plain:""},on:{click:t.ClickShellCheck}},[t._v("Shell Check")])],1)])],1),t._v(" "),a("el-col",{attrs:{span:15}},[a("el-row",{staticClass:"row-bg",attrs:{gutter:"20",type:"flex"}},[1==t.flag?a("div",[a("el-input",{staticStyle:{width:"400px"},attrs:{placeholder:"Address",clearable:""},model:{value:t.form.input,callback:function(e){t.$set(t.form,"input",e)},expression:"form.input"}}),t._v(" "),a("el-button",{staticClass:"n",attrs:{type:"danger"},on:{click:t.Submit1}},[t._v("Submit")])],1):t._e(),t._v(" "),2==t.flag?a("div",[a("el-input",{staticStyle:{width:"400px"},attrs:{placeholder:"Address",clearable:""},model:{value:t.form.input,callback:function(e){t.$set(t.form,"input",e)},expression:"form.input"}}),t._v(" "),a("el-button",{staticClass:"n",attrs:{type:"danger"},on:{click:t.Submit2}},[t._v("Submit")])],1):t._e(),t._v(" "),4==t.flag?a("div",[a("el-input",{staticStyle:{width:"400px"},attrs:{placeholder:"Shell",clearable:""},model:{value:t.form.input,callback:function(e){t.$set(t.form,"input",e)},expression:"form.input"}}),t._v(" "),a("el-button",{staticClass:"n",attrs:{type:"danger"},on:{click:t.Submit4}},[t._v("Submit")])],1):t._e()]),t._v(" "),a("el-row",{staticClass:"row-bg",attrs:{gutter:"20",type:"flex"}},[a("el-input",{staticStyle:{width:"500px"},attrs:{type:"textarea",rows:10,placeholder:"Result"},model:{value:t.result,callback:function(e){t.result=e},expression:"result"}})],1)],1)],1)],1)},staticRenderFns:[]};var p=l("VU/8")(c,u,!1,function(t){l("0jU9")},"data-v-26687ccc",null).exports;a.default.use(n.a);var d=new n.a({routes:[{path:"/",name:"HelloWorld",component:p}]}),f=l("zL8q"),h=l.n(f);l("tvR6");a.default.config.productionTip=!1,a.default.use(h.a),new a.default({el:"#app",router:d,components:{App:i},template:"<App/>"})},gsu9:function(t,e){},tGse:function(t,e,l){t.exports=l.p+"static/img/1.4641b05.jpg"},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.a0315ff6b66b0832420a.js.map