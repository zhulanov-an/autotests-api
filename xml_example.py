from xml.etree import ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <name>Akella</name>
    <age>225</age>
    <isStudent>true</isStudent>
    <email>zhu@jlj.com</email>
    <courses>
        <item>Python</item>
        <item>QA Engineer</item>
        <item>API Testing</item>
    </courses>
    <address>
        <city>Inno</city>
        <region>Tat</region>
        <zip>640500</zip>
    </address>
</person>
"""

root = ET.fromstring(xml_data)
courses = root.find('courses').findall('item')
for course in courses:
    print(course.text)