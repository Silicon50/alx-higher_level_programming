#!/usr/bin/node

const arg = process.argv;
const argLen = arg.length - 2;

if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
