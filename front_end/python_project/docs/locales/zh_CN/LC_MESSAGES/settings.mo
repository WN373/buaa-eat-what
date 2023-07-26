��                           	        '     .     @     Q  �   ]  �       �  !  �  8   �           1   &  *   X      �     �  *   �     �  %     -   2     `  !   {     �  �   �  ^   d	  *   �	     �	  7   �	  �   +
  �   �
  ,   v  �  �     *  	   1     ;     N     ^  �   e  �       �  �   �  8   �  �   �  	   �     �     �          *     =     S     f     v     �     �     �  �   �  B   w     �     �  !   �  �     �   �  *      Attribute Config Config serializer Config validator Description For the usage of these components, see `settings_interface.py <https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/settings/setting_interface.py>`_. Json files only support string, boolean value, list and dict, for enumeration classes or ``QColor``\ , we can't use ``json.dump()`` to write them directly into a json file, so PyQt-Fluent-Widgets provides ``ConfigSerializer`` and its subclass to serialize and deserialize config item from config file. For example, you can use ``ColorSerializer`` to serialize config items with ``QColor`` value type. Name of config item PyQt-Fluent-Widgets presents each configuration item as a ``SettingCard`` on the interface. The behavior of user on the ``SettingCard`` will change the value of the configuration item, and PyQt-Fluent-Widgets will update the configuration item to the json configuration file automatically. PyQt-Fluent-Widgets provides many kinds of setting card: PyQt-Fluent-Widgets uses the ``ConfigItem`` class to represent a configuration item and uses the ``QConfig`` class to read and write the value of ``ConfigItem``. The ``QConfig`` class will automatically update the configuration file when the value of the ``ConfigItem`` changes. Setting card Setting card for showing and managing folder list Setting card with a button to choose color Setting card with a color picker Setting card with a combo box Setting card with a group of radio buttons Setting card with a hyper link Setting card with a naive push button Setting card with a primary color push button Setting card with a slider Setting card with a switch button Settings Since the value in config file may be manually modified by the user to an invalid value, PyQt-Fluent-Widgets use ``ConfigValidator`` and its subclass to verify and correct the config value. The default value of config item, it will be used when the value in the config file is illegal The group to which the config item belongs Type Whether to restart the application after updating value You can use ``SettingCardGroup.addSettingCard()`` to add a setting card to the same group, and ``SettingCardGroup`` will adjust its layout automatically based on the height of setting cards. You should add config items to the class attribute of ``QConfig`` subclasss,  then use ``qconfig.load()`` to load config file, for example: ``ConfigItem`` has the following attributes: Project-Id-Version: PyQt-Fluent-Widgets 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2023-04-03 14:01+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_CN
Language-Team: zh_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0;
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.11.0
 属性 配置项 配置序列化器 配置校验器 描述 对于上述组件的具体使用方式，参见 `setting_interface.py <https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/settings/setting_interface.py>`_. PyQt-Fluent-Widgets 使用 json 文件来保存配置，而 json 文件只支持字符串、布尔值、列表和字典，对于枚举类或者 ``QColor``，无法直接将它们的值写入 json 文件中。为了解决这个问题，PyQt-Fluent-Widgets 提供了 ``ConfigSerializer`` 类及其子类来序列化和反序列化配置项。举个栗子，可以使用 `ColorSerializer` 来序列化值类型为 ``QColor`` 的配置项。 配置项的名字 PyQt-Fluent-Widgets 将每个配置项表示为界面的一个设置卡。用户在设置卡上的交互行为将会改变相应配置项的值，同时 PyQt-Fluent-Widgets 会自动更新配置文件。 PyQt-Fluent-Widgets 内置了许多类型的设置卡： PyQt-Fluent-Widgets 使用 ``ConfigItem`` 类来表示一个配置项，并使用 ``QConfig`` 类来读写 ``ConfigItem`` 项的值。当 ``ConfigItem`` 的值发生改变时，``QConfig`` 类会自动将配置项的值同步到配置文件中。 设置卡 文件夹列表设置卡 颜色选择按钮设置卡 拾色器设置卡 下拉框设置卡 单选按钮设置卡 超链接设置卡 按钮设置卡 主题色按钮设置卡 滑动条设置卡 开关按钮设置卡 设置 由于配置文件可能被用户手动篡改，导致配置项的值非法，所以 PyQt-Fluent-Widgets 使用 ``ConfigValidator`` 类及其子类来验证和修正配置项的值。 配置项的默认值，当配置值非法时将被默认值替代 配置项所属的组别 数据类型 配置更新后是否重启应用 可以通过 ``SettingCardGroup.addSettingCard()`` 将多个设置卡添加到同一个组中，``SettingCardGroup`` 会根据设置卡的高度自动调整自己的布局。 为了正确读写配置项的值，应该将 ``ConfigItem`` 的实例添加到 ``QConfig`` 子类的类属性中，然后使用 ``qconfig.load()`` 来加载配置文件。下面是一个简单的例子： ``ConfigItem`` 的属性如下表所示： 