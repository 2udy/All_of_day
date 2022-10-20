// 주어진 문자열이 회문인지 판별하는 isPalindrome 함수를 완성하시오.
function isPalindrome(str) {
  n = str.length
  revStr = ''
  for(i = n - 1; i >= 0; i--){
    if(str[i] != ' '){
      revStr += str[i]
    }
  }

  if (revStr == str.replaceAll(' ', '')){
    return true
  }else{
    return false
  }
}

// 출력
console.log(
  isPalindrome('a santa at nasa'),  // true
  isPalindrome('google')  // false
)