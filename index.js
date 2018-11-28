const ar = [1, 2, 1, 2, 1, 3, 2];
function sockMerchant(n, ar) {
  const obj = {};

  for (var i = 0; i < ar.length; i++) {
    obj[ar[i]] = obj[ar[i]] ? obj[ar[i]] + 1 : 1;
  }

  let total = 0;
  const colorsList = Object.keys(obj);
  for (var i = 0; i < colorsList.length; i++) {
    total += Math.floor(obj[colorsList[i]] / 2);
  }
  return total;
}
console.log(sockMerchant(ar.length, ar));
