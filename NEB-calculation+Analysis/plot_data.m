clear all
close all
delimiter=' '
initial=importdata('coords.lmps',delimiter,13);
x_ini=initial.data(:,3);
y_ini=initial.data(:,4);
z_ini=initial.data(:,5);

figure(1)
hold all
plot3(x_ini,y_ini,z_ini,'o')
plot3(x_ini(63),y_ini(63),z_ini(63),'x') %initiated pka
plot3(x_ini(188),y_ini(188),z_ini(188),'*') %initiated interstitial
title('Initial atom coordinates for neb calculation')
for i = 1:8
    eval(['fin',num2str(i),'=importdata(''pka188-min-',num2str(i),'.final'',delimiter,1);'])
    eval(['x_fin',num2str(i),'=fin',num2str(i),'.data(:,2);'])
    eval(['y_fin',num2str(i),'=fin',num2str(i),'.data(:,3);'])
    eval(['z_fin',num2str(i),'=fin',num2str(i),'.data(:,4);'])
    figure(i+1)
    hold all
    eval(['plot3(x_fin',num2str(i),',y_fin',num2str(i),',z_fin',num2str(i),',''o'')'])
    eval(['plot3(x_fin',num2str(i),'(63),y_fin',num2str(i),'(63),z_fin',num2str(i),'(63),''x'')'])
    eval(['plot3(x_fin',num2str(i),'(188),y_fin',num2str(i),'(188),z_fin',num2str(i),'(188),''*'')'])
    title('Final atom coordinates for neb calculation')
end
    