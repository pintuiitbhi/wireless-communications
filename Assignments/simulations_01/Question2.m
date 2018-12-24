t = linspace(-0.04,0.04,80);
Ts = 0.08/80;
Fs = 1/Ts;
Ta = 0.01;
mt2 = 2*sinc(2*t./Ta) + sinc((2*t./Ta)+1) + sinc((2*t./Ta)-1);
subplot(2,1,1);
figure(1)
plot(t,mt2);
title('Message signal m_{2}(t) (T_{a} = 0.01)')
xlabel('-0.04 < t < -0.04') % x-axis label
ylabel('m_{2}(t)') % y-axis label

fc = 300;
st = mt2.*cos(2*pi*fc*t);
% length(st)
subplot(2,1,2);
plot(t,st);
title(' DSB-SC modulated signal (time domain)')
xlabel('-0.04 < t < -0.04') % x-axis label
ylabel('s(t)') % y-axis label


%%%%%%%%%%%%%%%
L = length(st);
Mf = fft(mt2,L);
freq = (0:L-1).*(Fs/L);
freq_right = freq(freq < Fs/2);
freq_left = fliplr(-freq_right);
freq = [freq_left freq_right];

Mf_rignt = abs(Mf(1:round(L/2)));
Mf_left = fliplr(Mf_rignt);
Mf = [Mf_left Mf_rignt];
figure(2)
subplot(2,1,1);
% plot(freq_right, abs(xdft_rignt))
plot(freq, Mf)
title('Message signal (frequency domain)')
xlabel('frequency(hertz)') % x-axis label
ylabel('|M(f)|') % y-axis label

%%%%%%%%%%%
Sf = fft(st,L);
maxAmp = max(abs(Sf));
freq = (0:L-1).*(Fs/L);
freq_right = freq(freq < Fs/2);
freq_left = fliplr(-freq_right);
freq = [freq_left freq_right];

xdft_rignt = abs(Sf(1:round(L/2)));
xdft_left = fliplr(xdft_rignt);
xdft = [xdft_left xdft_rignt];
[maxVal, index] = max(xdft_rignt);
maxFreq = freq_right(index);

% plot(freq_right, abs(xdft_rignt))
subplot(2,1,2);
plot(freq, xdft)
title('DSB-SC Modulated Message signal (frequency domain)')
xlabel('frequency(hertz)') % x-axis label
ylabel('|S(f)|') % y-axis label
