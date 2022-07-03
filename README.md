# apidemo


#### back-end

```
pip install -r requirements.txt
python main.py
```

#### front-end

安装 nodejs [下载地址](https://nodejs.org/en/download/)

```
npm install
npm start
```

```
var app = new Vue({
            el: "#app",
            data: {
                // 定义列表结构
                list: [],
                // 是否使用mock数据
                mock: false,
            },
            mounted: function() {
                // 初始化页面调用 getPageList 方法   
                this.getPageList()
            },
            methods: {
                getPageList: function() {
                    if (this.mock) {
                        // mock 返回数据
                        this.list = [
                            {"name": "张三", "age": 14, "sex": 0},
                            {"name": "王四", "age": 19, "sex": 1},
                        ]
                    }else{
                        // 请求后台api返回数据    
                        fetch("http://localhost:5000/pagelist")
                            .then(res => res.json())
                            .then(res => {
                                if (res.code == 0) {
                                    this.list = res.data
                                } else {
                                    alert(res.msg)
                                }
                            })
                    }
                },
            }
        });
```

