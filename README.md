# 團隊開發遵從JavaScript Code Style原則

盡量遵從這份常用的JavaScript Code Style吧! 這樣在共同開發才不會很亂

這份是參考業界常用的JavaScript Code Style寫der

## 縮排
- 用兩個空格進行縮排，若習慣用Tab記得將你的編輯器（或IDE）的Tab自動轉空格，並設定Tab為兩空白

```javascript
if (collection.length) {
  a = 1;
}
```

## 括號位置
- 左括號一律在同一行，右括號一律在最後行，若是else則舊後括號與新左括號位於同一行

```javascript
if (collection.length) {
  if (test) {
  thing1();
  thing2();
} else {
  thing3();
}
```
## 空格
- 大括號前後空一格，等於前後空一格，運算子前後空一格

```javascript
if (true) {
  var x = y + 5;
}
```

## 命名規則
- 避免單字母命名。命名應具備描述性。

```javascript
// bad
function q() {
  // ...stuff...
}

// good
function query() {
  // ..stuff..
}
```

- 使用駝峰式命名對象、函數和實例。(字首小寫，後面新字接大寫，不要用底線）

```javascript
// bad
var OBJEcttsssss = {};
var this_is_my_object = {};
var o = {};
function c() {}

// good
var thisIsMyObject = {};
function thisIsMyFunction() {}
```

- 使用帕斯卡式命名構造函數或類。（字首大寫的駱駝峰）

```javascript
// bad
function user(options) {
  this.name = options.name;
}

var bad = new user({
  name: 'nope'
});

// good
function User(options) {
  this.name = options.name;
}

var good = new User({
  name: 'yup'
});
```

## 常用method命名
get與set方法必須明確定義，會回傳boolean值的方法需用is或has開頭


```javascript
// bad
dragon.age();

// good
dragon.getAge();

// bad
dragon.age(25);

// good
dragon.setAge(25);

// bad
if (!dragon.age()) {
  return false;
}

// good
if (!dragon.hasAge()) {
  return false;
}
```
以上為一般需要遵守，其他進階可參考[此來源](https://github.com/felixge/node-style-guide)
