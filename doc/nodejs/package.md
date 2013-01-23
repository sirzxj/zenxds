Node.js 在调用某个包时,会首先检查包中 package.json 文件的 main 字段,将其作为包的接口模块,如果 package.json 或 main字段不存在,会尝试寻找 index.js 或 index.node 作为包的接口。

package.json 是 CommonJS 规定的用来描述包的文件,完全符合规范的 package.json 文件应该含有以下字段。
* name:包的名称,必须是唯一的,由小写英文字母、数字和下划线组成,不能包含
空格。
* description:包的简要说明。
* version: keywords:关键字数组,通常用于搜索。
* maintainers:维护者数组,每个元素要包含 name、email (可选) web (可选)字段。
* contributors:贡献者数组,格式与maintainers相同。包的作者应该是贡献者
数组的第一个元素。
* bugs:提交bug的地址,可以是网址或者电子邮件地址。
* licenses:许可证数组,每个元素要包含 type (许可证的名称)和 url (链接到
许可证文本的地址)字段。
* repositories:仓库托管地址数组, 每个元素要包含 type(仓库的类型, git )如url (仓库的地址)和 path (相对于仓库的路径,可选)字段。
* dependencies:包的依赖,一个关联数组,由包名称和版本号组成。

## 把全局包当本地包来使用
	npm link express
	在 node_modules 子目录中发现一个指向安装到全局的包的符号链接

## npm init 根据交互式问答产生一个符合标准的 package.json

## debug
	安装 npm install -g node-inspector
	启动inspector服务 node-inspector & 
	以debug模式运行node.js应用 node --debug debug.js
	http://127.0.0.1:8080/debug?port=5858

