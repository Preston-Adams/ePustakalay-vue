(function(e){function t(t){for(var r,c,a=t[0],i=t[1],f=t[2],s=0,p=[];s<a.length;s++)c=a[s],Object.prototype.hasOwnProperty.call(o,c)&&o[c]&&p.push(o[c][0]),o[c]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);l&&l(t);while(p.length)p.shift()();return u.push.apply(u,f||[]),n()}function n(){for(var e,t=0;t<u.length;t++){for(var n=u[t],r=!0,c=1;c<n.length;c++){var i=n[c];0!==o[i]&&(r=!1)}r&&(u.splice(t--,1),e=a(a.s=n[0]))}return e}var r={},o={app:0},u=[];function c(e){return a.p+"static/management/js/"+({about:"about"}[e]||e)+".js"}function a(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.e=function(e){var t=[],n=o[e];if(0!==n)if(n)t.push(n[2]);else{var r=new Promise((function(t,r){n=o[e]=[t,r]}));t.push(n[2]=r);var u,i=document.createElement("script");i.charset="utf-8",i.timeout=120,a.nc&&i.setAttribute("nonce",a.nc),i.src=c(e);var f=new Error;u=function(t){i.onerror=i.onload=null,clearTimeout(s);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),u=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+r+": "+u+")",f.name="ChunkLoadError",f.type=r,f.request=u,n[1](f)}o[e]=void 0}};var s=setTimeout((function(){u({type:"timeout",target:i})}),12e4);i.onerror=i.onload=u,document.head.appendChild(i)}return Promise.all(t)},a.m=e,a.c=r,a.d=function(e,t,n){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)a.d(n,r,function(t){return e[t]}.bind(null,r));return n},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/",a.oe=function(e){throw console.error(e),e};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],f=i.push.bind(i);i.push=t,i=i.slice();for(var s=0;s<i.length;s++)t(i[s]);var l=f;u.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23"),o={id:"nav"},u=Object(r["e"])("Home"),c=Object(r["e"])(" | "),a=Object(r["e"])("About");function i(e,t,n,i,f,s){var l=Object(r["s"])("router-link"),p=Object(r["s"])("router-view");return Object(r["o"])(),Object(r["d"])(r["a"],null,[Object(r["f"])("div",o,[Object(r["f"])(l,{to:"/"},{default:Object(r["w"])((function(){return[u]})),_:1}),c,Object(r["f"])(l,{to:"/about"},{default:Object(r["w"])((function(){return[a]})),_:1})]),Object(r["f"])(p)],64)}n("64be");const f={};f.render=i;var s=f,l=(n("d3b7"),n("6c02")),p=n("cf05"),b=n.n(p),d={class:"home"},m=Object(r["f"])("img",{alt:"Vue logo",src:b.a},null,-1),v=Object(r["f"])("h1",null,"This is INDEX FILE",-1);function j(e,t,n,o,u,c){return Object(r["o"])(),Object(r["d"])("div",d,[m,v])}var O={name:"Home"};O.render=j;var h=O,g=[{path:"/",name:"Home",component:h},{path:"/about",name:"About",component:function(){return n.e("about").then(n.bind(null,"f820"))}}],y=Object(l["a"])({history:Object(l["b"])("/"),routes:g}),w=y,P=n("5502"),_=Object(P["a"])({state:{},mutations:{},actions:{},modules:{}});Object(r["c"])(s).use(_).use(w).mount("#app")},"64be":function(e,t,n){"use strict";n("c894")},c894:function(e,t,n){},cf05:function(e,t,n){e.exports=n.p+"static/management/img/logo.png"}});