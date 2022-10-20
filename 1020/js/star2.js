let star = ''
for(let i=1 ; i <= 5; i++){
  for(let j=5; j>=i; j--){
    star += ' '
  }
  for(let k = 1; k <= 2*i-1; k ++ ){
    star +='*'
  }
  star +='\n'
}
console.log(star)