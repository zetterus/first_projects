import streamlit as st
import streamlit.components.v1 as com


with open("not mine\streamlit test\designing.css") as source:
    design=source.read()
com.html(f""""
<div>
<style>
{design}
</style>
<h1 class="heading">
This is my Heading
</h1>
<p class=style>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit aliquet vehicula. Pellentesque nisi lectus, tempus ac blandit vitae, fermentum ut ligula. Integer imperdiet, turpis ut blandit bibendum, erat massa mattis ex, sit amet condimentum nisl eros in justo. Sed venenatis odio et enim ultrices placerat. In id aliquet dui. In porttitor at eros nec ornare. Nam sem ex, rutrum vitae quam sed, eleifend interdum ligula. Donec faucibus lacinia est, ac tempus augue rutrum et. Morbi molestie pulvinar lectus ut porta. Donec rhoncus fermentum enim, nec porttitor ex vehicula eget. Proin fermentum posuere lorem. Aenean rhoncus tellus quis dapibus fermentum. Aenean id finibus sapien.

Morbi dignissim ut quam ut finibus. Fusce non augue justo. Quisque vehicula, nulla sed pretium ultrices, dolor orci finibus risus, porta sollicitudin dui sapien in erat. In a pellentesque dolor. Mauris in felis lobortis magna laoreet posuere ac nec urna. Aliquam erat volutpat. Aenean sodales, quam vitae viverra vestibulum, lorem lacus gravida metus, in semper turpis nulla nec purus. Etiam blandit dignissim massa, eget tincidunt dolor bibendum eu.

Proin eu hendrerit sem. Praesent tempus tristique neque, eget scelerisque ipsum finibus in. Etiam a ultricies urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum ac sagittis purus, in mollis lorem. Nam blandit finibus sapien, id maximus orci fermentum a. Morbi vestibulum massa elit, mollis convallis nunc lacinia nec. Donec ut urna sed tellus sollicitudin aliquet. Proin sit amet sapien vel dolor tempus euismod at ut nunc. Aliquam blandit leo sed cursus lobortis.

Duis ac turpis lacinia, sollicitudin lacus ut, accumsan risus. Donec eu nisl ante. Curabitur venenatis malesuada risus, consectetur cursus augue viverra sit amet. In ac euismod nisi, vitae fringilla sem. Morbi imperdiet nisi augue, nec pellentesque dolor auctor id. Sed malesuada tristique viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec eget dolor sit amet tortor semper egestas nec in augue. Praesent ac augue in risus ultrices dictum. Curabitur porta mi eget mauris feugiat porta. Quisque eu imperdiet lacus. Vivamus scelerisque pretium congue. Fusce sit amet consectetur ante. In hac habitasse platea dictumst.

Sed ut lorem at justo vestibulum ultricies sit amet sed erat. Mauris posuere orci risus, et pellentesque metus pellentesque id. Phasellus et risus nisl. Cras dapibus metus at orci placerat imperdiet. Quisque a pharetra mi. Duis lobortis metus ac nisl interdum vestibulum. Mauris eros lectus, dictum nec fermentum eget, malesuada sed quam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum tempor aliquam dictum.
</p>
</div>
""", height=400, scrolling=True)

com.iframe("https://lottie.host/embed/955ab029-2480-492f-9471-a358679c37c3/XymmgJspNh.json")
