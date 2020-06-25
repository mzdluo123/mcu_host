# mcu_host
python实现的简单单片机上位机程序

其中下位机是Arduino单片机

```c
int IN1 = PD3;  
int IN2 = PD4;
int ENA = PD5;

#define STATE_WAIT 0
#define STATE_PWM 254
#define STATE_DIRECTION 253 
#define CMD_PWM 1
#define CMD_DIRECTION 2
#define REGHT_DIRECTION 1
#define LEFT_DIRECTION 2


void setup() {
	Serial.begin(9600);
	//sets the pin as output
	pinMode(IN1, OUTPUT);
	pinMode(IN2, OUTPUT);
	pinMode(LED_BUILTIN, OUTPUT);

	//set direction；
	digitalWrite(IN1, HIGH);
	digitalWrite(IN2, LOW);
	while (Serial.read()>=0)  //清除buffer
	{
	}
	
}

void loop() {
	u8 state = STATE_WAIT;
	while (1) {
		while (Serial.available() > 0) {
			u8 data = Serial.read();
			switch (state)
			{
			case STATE_PWM:	
				analogWrite(ENA, data);
				state = STATE_WAIT;
				break;

			case STATE_DIRECTION:
				if (data == REGHT_DIRECTION) {
					digitalWrite(IN1, HIGH);
					digitalWrite(IN2, LOW);
				}
				else {
					digitalWrite(IN1, LOW);
					digitalWrite(IN2, HIGH);
				}
				state = STATE_WAIT;
				break;

			case STATE_WAIT:
				switch (data)
				{
				case CMD_PWM:
					state = STATE_PWM;
					break;

				case CMD_DIRECTION:
					state = STATE_DIRECTION;
					break;

				default:
					break;
				}
				break;
			default:
				break;
			}
		
		}
	}
	
}


```