fs=10;  % Sampling frequency (in hertz)
fa=0.05;    % Frequency of message signal
Ta=1/(fa);   % Time period of message signal
fc=0.4; % Frequency of carrier signal
Tc=1/fc;    % Time period of carrier signal
t=linspace(0,10*Ta,200*fs);   % Total time for simulation

%-------------------- Carrier Signal --------------------%
Ac=1; % Amplitude of carrier signal [ where, modulation Index (m)=Am/Ac ]
yc=Ac*cos(2*pi*fc*t);   % Eqation of carrier signal
plot(t,yc), grid on;    % Graphical representation of carrier signal
title ( ' Plot of Carrier Signal   ');
xlabel ( ' Time(sec) ');
ylabel (' Amplitude(volt) ');

c = 1;
%-------------------- AM modulation Index --------------------%
for i =[0.5 1 2]
    m = i;
    
    %-------------------- Message Signal --------------------%
    Am=m*Ac;   % Amplitude of message signal
    ym=Am*cos(2*pi*fa*t);  % Eqaution of message signal
    figure(c)
    subplot(4,1,1); 
    plot(t,ym), grid on; % Graphical representation of Message signal
    title ( [' Message Signal (time domain)  \mu = ', num2str(m)]);
    xlabel ( ' time(sec) ');
    ylabel (' m_{1}(t)   ');

    %-------------------- AM Modulation --------------------% 
    s=Ac*(1+m*cos(2*pi*fa*t)).*cos(2*pi*fc*t); % Equation of Amplitude modulated signal
    figure(c)
    subplot(4,1,2); % Graphical representation of AM signal
    plot(t,ym+1);
    hold on
    plot(t,-ym-1);
    hold on
    plot(t,s);
    title ( ['  Amplitude Modulated signal (time domain) \mu = ', num2str(m)]);
    xlabel ( ' time(sec) ');
    ylabel ('s(t)   ');
    grid on;

    %-------------------- Fourier Transform of Message signal --------------------%
    L = length(t);
    fftSignal = fft(ym,L);  % finding the fourier transform
    fftSignal = fftshift(fftSignal);    % shifting zero-frequency component to center of spectrum
    f = (-L/2: L/2-1).*fs/L;
    figure(c)
    subplot(4,1,3);
    plot(f,abs(fftSignal)); % Graphical representation of Fourier Transform of Message signal
    title ([ '  Message Signal (frequency domain) \mu = ', num2str(m)]);
    xlabel ( ' frequency(hertz) ');
    ylabel (' |M(f)|   ');

    %-------------------- Fourier Transform of Modulated signal --------------------%
    fft_s = fftshift(fft(s));   % finding the fourier transform and 
                                % shifting zero-frequency component to center of spectrum
    figure(c)
    subplot(4,1,4);
    plot(f,abs(fft_s)); % Graphical representation of Fourier Transform of Modulated signal
    title ( ['  Amplitude Modulated signal (frequency domain)  \mu = ', num2str(m)]);
    xlabel ( ' frequency(hertz) ');
    ylabel (' |S(f)| ');
    
    c = c+1;
end

