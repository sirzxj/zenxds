## Model
	* rules: 对模型属性的验证规则,自定义的规则要在模型里实现一个同名方法
	* relations: 关联的对象(表结构关系)
	* attributeLabels: 表结构对应的lable的名字
	* getUrl: like Django get_absolute_url($post->url)
	* behavior

## Controller:
	* filters: 过滤器,配置在控制器动作执行之前或之后执行
	* accessRules: 访问控制

## View

## Model Methods
	$project = Project::model()->findByPk(1);
	findAll()
	findByAttributes(array('id'=>$id))
	saveAttributes(array())