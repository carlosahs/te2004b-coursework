# DSP
It is a tool to manipulate signals after ADC.
## Applications
* Analysis of EEG, ECG
* Digital photography
## Types
* Adaptive filters
# Continous signals
## Mathematical description
$$
x(t) = \sin(\omega t) = \sin(2 \pi f_o t)
$$
$$
x[n] = \sin(2 \pi f_o n t s)
$$
# Unit pulse
$$
\delta = \int_{-\infty}^{\infty} \delta \mathrm{d}t = 1
$$
## Discrete unit pulse
$$
y[n] = \delta[n - 1]
$$
# Linear Time Invariant (LTI)
Superposition of the outputs of each input if the inputs would've been
inputted individually.
$$
x_1[n] \to \text{DSP} \to y_1[n]
x_2[n] \to \text{DSP} \to y_2[n]
x_1[n] + x_2[n] \to \text{DSP} \to y_1[n] + y_2[n]
$$
## Time invariant
A time delay or shift in the input causes an equivalent time delay in
the system's output
$$
x[n] \to \text{DSP} \to y[n]
x[n - 1] \to \text{DSP} \to y[n - 1]
$$
# Difference equations (see all of the above)
# Shannon's theorem
# Nyquist frequency
