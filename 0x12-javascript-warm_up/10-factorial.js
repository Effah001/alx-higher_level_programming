#!/usr/bin/node

function factorial () {
  const num = Number(process.argv[2]);

  if (!isNaN(num) && num >= 0) {
    let fac = 1;
    for (let i = 1; i <= num; i++) {
      fac *= i;
    }
    console.log(fac);
  } else {
    console.log('1');
  }
}
factorial();
