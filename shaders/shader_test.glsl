
uniform vec2 lightPosition;
uniform float lightSize;

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{

    float distanceToLight = length(lightPosition - fragCoord);


    vec2 normalizedFragCoord = fragCoord/iResolution.xy;


    float lightAmount = 1.0;


    lightAmount *= 1.0 - smoothstep(0.0, lightSize, distanceToLight);


    vec4 blackColor = vec4(0.0, 0.0, 0.0, 1.0);


    fragColor = mix(blackColor, texture(iChannel1, normalizedFragCoord), lightAmount);
}