L1 = 40;
L2 = 104.6;
L3 = 104.6;
L4 = 91;
L(1) = Link('revolute','qlim',[0 pi],'d',L1,'a',0,'alpha',pi/2,'offset',0);
L(2) = Link('revolute','qlim',[0 pi],'d',0,'a',L2,'alpha',0,'offset',0);
L(3) = Link('revolute','qlim',[0 pi],'d',0,'a',L3,'alpha',0,'offset',0);
L(4) = Link('revolute','qlim',[0 pi],'d',0,'a',L4,'alpha',-pi/2,'offset',0);

ROBOT = SerialLink(L,'name','Rob');
ROBOT.tool = transl(0,0,0);
%%
figure(1)
ROBOT.plot([0 0 0 0],'notiles','noname');

%%
%Hallamos las MTH
syms q1 q2 q3 q4
H10 = trotz(q1)*transl(L1,0,0)*transl(0,0,0)*trotx(pi/2)
H21 = trotz(q2)*transl(0,0,0)*transl(L2,0,0)*trotx(0)
H32 = trotz(q3)*transl(0,0,0)*transl(L3,0,0)*trotx(0)
H43 = trotz(q4)*transl(0,0,0)*transl(0,0,0)*trotx(pi/2)
H40 = H10*H21*H32*H43

%%
q1 = 0;
q2 = 0;
q3 = 0;
q4 = 0;
MTH_TCP = subs(H40);

%figure(2)
%ROBOT.plot([q_1 q_2 q_3 q_4],'notiles','noname');


%q = ROBOT.ikine(T,'q0',[0 0 0 0],'mask',[1 1 1 1 0 0])
%% 
%Triangulo

Puntos = [-40 230 40; 10 230 40; 10 250 40];
Ql = [];
for i = 1:3
    cla
    x = Puntos(i,1);
    y = Puntos(i,2);
    z = Puntos(i,3);
    D = sqrt(x^2+y^2);
    beta = atan((z-L1)/D);
    r = sqrt(D^2-z^2);
    cosAlfa = (r-L4)/(2*L2);
    sinAlfa = sqrt(1-cosAlfa^2);
    Alfa = atan2(sinAlfa,cosAlfa);
    q_1 = atan2(y,x);
    q_2 = Alfa+beta;
    cosQ3 = ((r-L4)^2/(2*L2^2))-1;
    sinQ3 = sqrt(1-cosQ3^2);
    q_3 = -atan2(sinQ3,cosQ3);
    q_4 = Alfa;
    Q = [q_1 q_2 q_3 q_4];%*(180/pi);
    Ql = [Ql;Q];
    ROBOT.plot(Q,'notiles','noname');
end
XYz = ROBOT.fkine(Ql(1,:))
