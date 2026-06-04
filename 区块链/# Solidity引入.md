# Solidity引入

~~~
// SPDX-License-Identifier: MIT    // 使用的软件许可，MIT
pragma solidity ^0.8.21;  // 版本
contract HelloWeb3{       // 合约
    string public _string = "Hello Web3!";
}

~~~

# 值

## 布尔值

~~~
// 布尔值
bool public _bool = true;
// 布尔运算
bool public _bool1 = !_bool; // 取非
bool public _bool2 = _bool && _bool1; // 与
bool public _bool3 = _bool || _bool1; // 或
bool public _bool4 = _bool == _bool1; // 相等
bool public _bool5 = _bool != _bool1; // 不相等

~~~

## int

~~~
// 整型
int public _int = -1; // 整数，包括负数
uint public _uint = 1; // 无符号整数
uint256 public _number = 20220330; // 256位无符号整数

~~~

## 地址类型

~~~
// 地址
address public _address = 0x7A58c0Be72BE218B41C608b7Fe7C5bB630736C71;
address payable public _address1 = payable(_address); // payable address，可以转账、查余额
// 地址类型的成员
uint256 public balance = _address1.balance; // balance of address

~~~

## 定长字节数组

-   定长字节数组: 属于值类型，数组长度在声明之后不能改变。根据字节数组的长度分为 `bytes1`, `bytes8`, `bytes32` 等类型。定长字节数组最多存储 32 bytes 数据，即`bytes32`。
-   不定长字节数组: 属于引用类型（之后的章节介绍），数组长度在声明之后可以改变，包括 `bytes` 等。

~~~
// 固定长度的字节数组
bytes32 public _byte32 = "MiniSolidity"; 
bytes1 public _byte = _byte32[0]; 

~~~

# 函数

~~~
function <function name>([parameter types[, ...]]) {internal|external|public|private} [pure|view|payable] [virtual|override] [<modifiers>]
[returns (<return types>)]{ <function body> }


~~~

1.   `function`：声明函数时的固定用法。要编写函数，就需要以 `function` 关键字开头。
2.   `<function name>`：函数名。
3.   `([parameter types[, ...]])`：圆括号内写入函数的参数，即输入到函数的变量类型和名称。
4.   `{internal|external|public|private}`：函数可见性说明符，共有4种。
    -   `public`：内部和外部均可见。
    -   `private`：只能从本合约内部访问，继承的合约也不能使用。
    -   `external`：只能从合约外部访问（但内部可以通过 `this.f()` 来调用，`f`是函数名）。
    -   `internal`: 只能从合约内部访问，继承的合约可以用。
5.  `[pure|view|payable]`：决定函数权限/功能的关键字。`payable`（可支付的）很好理解，带着它的函数，运行的时候可以给合约转入 ETH。`pure` 和 `view` 的介绍见下一节。 
6.  `[virtual|override]`: 方法是否可以被重写，或者是否是重写方法。`virtual`用在父合约上，标识的方法可以被子合约重写。`override`用在自合约上，表名方法重写了父合约的方法。
7.  `<modifiers>`: 自定义的修饰器，可以有0个或多个修饰器。
8.  `[returns ()]`：函数返回的变量类型和名称。
9.  `<function body>`: 函数体。



~~~
// 默认function
function add() external{
    number = number + 1;
}
这个是错误的，会被默认为pure不能读取状态变量也不改变变量
// pure: 纯纯牛马
function addPure(uint256 _number) external pure returns(uint256 new_number){
    new_number = _number + 1;
}
在 Solidity 中，“读取”特指访问合约的状态变量。
**状态变量**：这些是直接在合约中、函数外部声明的变量（例如 uint256 public number = 5;）。它们的值被永久存储在区块链上，构成了合约的持久化“状态”。
**局部变量**：这些是在函数内部声明的变量（例如 addPure 函数中的 new_number 或参数 _number）。它们只在函数执行期间临时存在，存储在内存（memory）或调用数据（calldata）中，函数执行完毕后就会被销毁，不属于合约的链上状态。
因此，访问局部变量或函数参数不被视为“读取”链上状态。
~~~



-   `view`只能读不能改写

~~~
// view: 看客
function addView() external view returns(uint256 new_number) {
    new_number = number + 1;
}
~~~





## `pure`和`view`

-   “纯”
-   “看”

刚开始学习 `solidity` 时，`pure` 和 `view` 关键字可能令人费解，因为其他编程语言中没有类似的关键字。`solidity` 引入这两个关键字主要是因为 以太坊交易需要支付气费（gas fee）。合约的状态变量存储在链上，gas fee 很贵，如果计算不改变链上状态，就可以不用付 `gas`。包含 `pure` 和 `view` 关键字的函数是不改写链上状态的，因此用户直接调用它们是不需要付 gas 的（注意，==合约中非 `pure`/`view` 函数调用 `pure`/`view` 函数时需要付gas）==。

`pure` 函数确实**不能读取** `public` 的状态变量。

## 修改链上的状态

1.  写入状态变量。
2.  释放事件。
3.  创建其他合约。
4.  使用 `selfdestruct`.
5.  通过调用发送以太币。
6.  调用任何未标记 `view` 或 `pure` 的函数。
7.  使用低级调用（low-level calls）。
8.  使用包含某些操作码的内联汇编。

## `internal v.s. external`

~~~
contract Demo {
    uint256 public number = 10;

    // internal: 只有这个合约自己（或继承它的合约）能看见
    function minus() internal {
        number = number - 1;
    }

    // external: 外部可以调用
    function minusCall() external {
        // 这里是在合约内部调用，所以可以直接用 minus()
        minus(); 
    }
}
~~~

## `pagable`

~~~
// payable: 递钱，能给合约支付eth的函数
function minusPayable() external payable returns(uint256 balance) {
    minus();    
    balance = address(this).balance;
}

~~~

我们定义一个 `external payable` 的 `minusPayable()` 函数，间接的调用 `minus()`，并且返回合约里的 ETH 余额（`this` 关键字可以让我们引用合约地址）。我们可以在调用 `minusPayable()` 时往合约里转入1个 ETH。

## `返回值：return 和 returns`

-   `returns`：跟在函数名后面，用于声明返回的变量类型及变量名。
-   `return`：用于函数主体中，返回指定的变量。

~~~
// 返回多个变量
function returnMultiple() public pure returns(uint256, bool, uint256[3] memory){
    return(1, true, [uint256(1),2,5]);
}

~~~

在上述代码中，我们利用 `returns` 关键字声明了有多个返回值的 `returnMultiple()` 函数，然后我们在函数主体中使用 `return(1, true, [uint256(1),2,5])` 确定了返回值。

这里`uint256[3]`声明了一个长度为`3`且类型为`uint256`的数组作为返回值。因为`[1,2,3]`会默认为`uint8(3)`，因此`[uint256(1),2,5]`中首个元素必须强转`uint256`来声明该数组内的元素皆为此类型。数组类型返回值默认必须用memory修饰，在下一个章节会细说

# 返回

我们可以在 `returns` 中标明返回变量的名称。Solidity 会初始化这些变量，并且自动返回这些变量的值，无需使用 `return`。

~~~
// 命名式返回
function returnNamed() public pure returns(uint256 _number, bool _bool, uint256[3] memory _array){
    _number = 2;
    _bool = false;
    _array = [uint256(3),2,1];
}
~~~

-   也可以直接用元组合起来

```
// 命名式返回，依然支持return
function returnNamed2() public pure returns(uint256 _number, bool _bool, uint256[3] memory _array){
    return(1, true, [uint256(1),2,5]);
}
```

# 数据存储

-   Solidity数据存储位置有三类：`storage`，`memory`和`calldata`。

-   不同存储位置的`gas`成本不同。

    -   `storage`类型的数据存在链上，类似计算机的硬盘，消耗`gas`多；

    -   `memory`和`calldata`类型的临时存在内存里，消耗`gas`少。
    -   整体消耗`gas`从多到少依次为：`storage` > `memory` > `calldata`。大致用法：

**默认是** 

```
storage
```

函数里的参数和临时变量一般用

~~~memory~~~
memory
~~~

calldata 存储在内存中，不上链,**不能修改**

~~~
function fCalldata(uint[] calldata _x) public pure returns(uint[] calldata){
    //参数为calldata数组，不能被修改
    // _x[0] = 0 //这样修改会报错
    return(_x);
}

~~~

# 声明

~~~
uint[] x = [1,2,3]; // 状态变量：数组 x

function fStorage() public{
    //声明一个storage的变量 xStorage，指向x。修改xStorage也会影响x
    uint[] storage xStorage = x;
    xStorage[0] = 100;
}

~~~

# 作用域

-   状态
-   局部
-   全局

状态变量是数据存储在链上的变量，所有合约内函数都可以访问，`gas`消耗高。状态变量在合约内、函数外声明：

~~~
contract Variables {
    uint public x = 1;
    uint public y;
    string public z;
}

function foo() external{
    // 可以在函数里更改状态变量的值
    x = 5;
    y = 2;
    z = "0xAA";
}

~~~

局部变量是仅在函数执行过程中有效的变量，函数退出后，变量无效。局部变量的数据存储在内存里，不上链，`gas`低。局部变量在函数内声明：

~~~
function bar() external pure returns(uint){
    uint xx = 1;
    uint yy = 3;
    uint zz = xx + yy;
    return(zz);
}

~~~

全局变量是全局范围工作的变量，都是`solidity`预留关键字。他们可以在函数内不声明直接使用：

~~~
function global() external view returns(address, uint, bytes memory){
    address sender = msg.sender;
    uint blockNum = block.number;
    bytes memory data = msg.data;
    return(sender, blockNum, data);
}

~~~

## 以太时间和时间单位

#### 以太单位

`Solidity`中不存在小数点，以`0`代替为小数点，来确保交易的精确度，并且防止精度的损失，利用以太单位可以避免误算的问题，方便程序员在合约中处理货币交易。

-   `wei`: 1
-   `gwei`: 1e9 = 1000000000
-   `ether`: 1e18 = 1000000000000000000

#### 时间单位

可以在合约中规定一个操作必须在一周内完成，或者某个事件在一个月后发生。这样就能让合约的执行可以更加精确，不会因为技术上的误差而影响合约的结果。因此，时间单位在`Solidity`中是一个重要的概念，有助于提高合约的可读性和可维护性。

-   `seconds`: 1
-   `minutes`: 60 seconds = 60
-   `hours`: 60 minutes = 3600
-   `days`: 24 hours = 86400
-   `weeks`: 7 days = 604800

# 数组&结构体

-   固定长度:在声明时指定数组的长度。用`T[k]`的格式声明，其中`T`是元素的类型，`k`是长度

~~~
// 固定长度 Array
uint[8] array1;
bytes1[5] array2;
address[100] array3;

~~~

-    可变长度数组（动态数组）：在声明时不指定数组的长度。用`T[]`的格式声明，其中`T`是元素的类型，例如：

~~~
// 可变长度 Array
uint[] array4;
bytes1[] array5;
address[] array6;
bytes array7;

~~~

## 方法

-   `length`: 数组有一个包含元素数量的`length`成员，`memory`数组的长度在创建后是固定的。
-   `push()`: `动态数组`拥有`push()`成员，可以在数组最后添加一个`0`元素，并返回该元素的引用。
-   `push(x)`: `动态数组`拥有`push(x)`成员，可以在数组最后添加一个`x`元素。
-   `pop()`: `动态数组`拥有`pop()`成员，可以移除数组最后一个元素。

## 结构体

~~~
// 结构体
struct Student{
    uint256 id;
    uint256 score; 
}

Student student; // 初始一个student结构体

~~~

## 赋值

~~~
//  给结构体赋值
// 方法1:在函数中创建一个storage的struct引用
function initStudent1() external{
    Student storage _student = student; // assign a copy of student
    _student.id = 11;
    _student.score = 100;
}

// 方法2:直接引用状态变量的struct
function initStudent2() external{
    student.id = 1;
    student.score = 80;
}

// 方法3:构造函数式
function initStudent3() external {
    student = Student(3, 90);
}

// 方法4:key value
function initStudent4() external {
    student = Student({id: 4, score: 60});
}

~~~

