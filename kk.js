let field = document.querySelector('#divContent')
let divs = field.querySelectorAll('div[topic].field:not(qtoipc)')
divs = Array.from(divs)
let single = divs.filter(div => div.getAttribute('type') === '3')
let singleRadio = divs.filter(div => div.getAttribute('type') === '5')
let multi = divs.filter(div => div.getAttribute('type') === '4')

setInterval(()=>{
  let cancel = document.querySelector('.layui-layer.layui-layer-dialog .layui-layer-btn1')
  if(cancel){
    cancel.click()
  }
}, 100)

function getRandomInt(max){
  return Math.floor(Math.random() * max)
}

function processSingle(div){
  let radios = div.querySelectorAll('div.label')
  console.log(radios)
  radios[getRandomInt(radios.length)].click()
}

function processSingleRadio(div){
  let lis = div.querySelectorAll('li.td')
  lis[getRandomInt(lis.length)].click()
}

function processMulti(div){
  let lis = div.querySelectorAll('div.label')
  let count = getRandomInt(lis.length) + 2
  for(let i = 0; i < count; i++){
    lis[i].click()
  }
}

function main(){
  single = Array.from(single)
  singleRadio = Array.from(singleRadio)
  multi = Array.from(multi)

  single.forEach(x=>processSingle(x))
  singleRadio.forEach(x=>processSingleRadio(x))
  multi.forEach(x=>processMulti(x))
}
main()
setTimeout(()=>{
  main()
}, 500)