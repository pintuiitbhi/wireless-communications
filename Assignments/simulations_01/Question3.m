% defining the given parameters of message signal %
fs = 12500;  % Sampling frequency (in hertz)
t = -0.04:ts:0.04;  % Total time for simulation
Ta = 0.01;  % Time period of message signal

%-------------------- Message Signal  --------------------%
m_t = triangularPulse((t+0.01)/0.01) - triangularPulse((t-0.01)/0.01); % Eqaution of message signal
figure(1)
subplot(221);
plot(t,m_t);    % Graphical representation of Message signal
title('Message Signal (time domain)');
xlabel('{\it t} (sec)');
ylabel('{\it m}({\it t})');

%-------------------- Modulated Signal --------------------% 
s_t = m_t.*cos(2*pi*300*t); % Equation of modulated signal
subplot(223);
plot(t,s_t);  % Graphical representation of modulated signal
title('Modulated Signal (time domain)');
xlabel('{\it t} (sec)');
ylabel('{\it s}_{\rm m}({\it t})');

%-------------------- Message Signal (frequency domain) --------------------%
L = length(s_t);
m_f = fftshift(fft(m_t,L));
f = (-L/2:L/2-1).*(fs/L);
Frange = [-600 600 0 200];
subplot(222);
plot(f,abs(m_f));    % Graphical representation of Message signal
axis(Frange);
title('Message Signal (frequency domain)');
xlabel('{\it f} (Hz)');
ylabel('{\it M}({\it f})');

%-------------------- Modulated Signal (frequency domain) --------------------%
s_f = fftshift(fft(s_t,L));
subplot(224);
plot(f,abs(s_f));    % Graphical representation of Modulated signal
axis(Frange);
title('Modulated Signal (frequency domain)');
xlabel('{\it f} (Hz)');
ylabel('{\it S}_{m}({\it f})');


Hf= rectangularPulse(-300,300,f);
Hff = fftshift(Hf);
figure(2);
plot(f, Hf);
title('Low pass filter H(f)');
xlabel('f'); % x-axis label
ylabel('|H(f)|'); % y-axis label


yt = s_t.*cos(2*pi*300*t);
figure(3);
subplot(211);
plot(t,yt);
title('Demodulated Signal');
xlabel('t'); % x-axis label
ylabel('y(t)'); % y-axis label

yf1 = fft(yt,length(yt));
yf = fftshift(fft(yt,length(yt)));
subplot(212);
plot(f,abs(yf));
axis(Frange);
title('Demodulated Signal (frequency domain)');
xlabel('f'); % x-axis label
ylabel('y(f)'); % y-axis label

rec_sig = yf1.*Hff;
figure(4);
plot(t,ifft(rec_sig))
title('Recovered Signal')
xlabel('t') % x-axis label
ylabel('y(t)') % y-axis label




