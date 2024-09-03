# soap
무게가 서로 다른 골드바를 여러 개의 포대에 나눠서 담으려고 합니다. 이 때 가장 무거운 포대와 가장 가벼운 포대의 무게 차이를 최소가 되도록 담는 것이 목표입니다.
골드바들의 무게가 저장된 배열과 포대의 개수가 주어지고, 골드바를 나누어 담을 때, 최소 무게와 최대 무게의 차이를 반환하는 solution() 함수를 완성하세요.
$solution()$ 의 입력으로는 다음과 같은 것들이 주어집니다.
•	$m$: 골드바들의 무게가 담긴 배열
•	k:  포대의 개수
제한사항
•	골드바의 수는 2 이상 10 이하입니다.
•	골드바의 무게의 범위는 1 이상 1,000,000,000 이하이며, 정수입니다.
•	배열 m 은 정렬되지 않은 상태로 주어집니다.
•	k 의 범위는 2 이상 5 이하입니다.
•	포대 자체는 무게가 0이고, 크기 제한도 없습니다.

입출력 예
m	k	answer
(1,4,2,5)	2	0
(2,1,4,5,3,1)	3	1
입출력 예 설명
입출력 예 #1
m =(1,4,2,5)에 대해 k=2이므로 아래와 같이 나누면 각 포대의 무게가 같습니다.
•	(1,5), (2,4)
각 포대의 무게는 모두 6으로서, 차이가 0이기 때문에 0을 반환합니다.

입출력 예 #2
m =(2,1,4,5,3,1)에 k=3이므로 아래와 같이 3개로 나누어 볼 수 있습니다. 
•	(2,3), (1, 4), (5, 1)
각 포대의 무게는 5, 5, 6으로서 최대와 최소의 차이는 1입니다. 따라서 1을 반환합니다.
이 때 전체 무게의 합은 16으로서 k=3으로 나누게 되면 나누어 떨어지지 않기 때문에 최대와 최소의 차이는 적어도 1이 나온다는 것을 알 수 있고, 현재 차이가 1인 배치 방법을 제시하였기에 이 차이가 최소임을 알 수 있습니다.
채점 방식
이 문제의 채점에는 정확성 테스트가 적용됩니다.
•	정확성 테스트: 제출한 알고리즘에 각 테스트 케이스를 적용하여 올바른 출력이 얻어지는지 확인합니다. 단, 알고리즘의 실행이 10초 이내에 종료되지 않는 경우(무한 반복 포함) "시간 초과" 로 실패합니다.

Greedy 알고리즘 실패 사례
m=(5,5,4,4,4,4,2,2), k=3
(5, 4, 2), (5, 4), (4, 4, 2) => 무게차이 2
최적해 (5, 5), (4, 4, 2), (4, 4, 2) => 무게차이 0
